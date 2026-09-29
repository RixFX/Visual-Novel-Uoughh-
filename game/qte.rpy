init python:
    import random

    QTE_BUTTON_SIZE = 160
    QTE_RING_START  = 300
    QTE_DURATION    = 0.9
    QTE_HIT_WINDOW  = 60
    QTE_HOLD_TIME   = 0.6
    QTE_MARGIN      = 120

    QTE_SFX_HIT  = "audio/hit.ogg"
    QTE_SFX_MISS = "audio/miss.ogg"

    QTE_FONT       = "fonts/DiarioDeAndy-L3ADy.otf"
    QTE_ICON_IMG   = "images/qte/x.png"
    QTE_ICON_SIZE  = 80
    QTE_TEXT_HIT   = "UOUGH"
    QTE_TEXT_MISS  = "MISS"
    QTE_TEXT_SIZE  = 48
    QTE_COLOR_HIT  = "#4ade80"
    QTE_COLOR_MISS = "#f87171"

    class QTEButton(object):
        def __init__(self, cx, cy, delay):
            self.cx          = cx
            self.cy          = cy
            self.delay       = delay
            self.started     = False
            self.start_time  = None
            self.result      = None
            self.result_time = None
            self.visible     = True

        def progress(self, st):
            if self.start_time is None:
                return 0.0
            return min((st - self.start_time) / QTE_DURATION, 1.0)

        def ring_size(self, st):
            return QTE_RING_START + (QTE_BUTTON_SIZE - QTE_RING_START) * self.progress(st)


    class QTEMultiDisplayable(renpy.Displayable):
        def __init__(self, buttons):
            super(QTEMultiDisplayable, self).__init__()
            self.buttons      = buttons
            self.global_start = None

        def all_done(self):
            return all(b.result is not None for b in self.buttons)

        def results(self):
            return [b.result for b in self.buttons]

        def render(self, width, height, st, at):
            r = renpy.Render(width, height)

            if self.global_start is None:
                self.global_start = st

            elapsed_global = st - self.global_start
            need_redraw    = False

            for btn in self.buttons:

                if elapsed_global < btn.delay:
                    need_redraw = True
                    continue

                if btn.start_time is None:
                    btn.start_time = st

                if not btn.visible:
                    continue

                prog      = btn.progress(st)
                ring_sz   = btn.ring_size(st)
                in_window = ring_sz <= QTE_BUTTON_SIZE + QTE_HIT_WINDOW
                cx        = btn.cx
                cy        = btn.cy
                bs        = QTE_BUTTON_SIZE

                if prog >= 1.0 and btn.result is None:
                    btn.result      = "miss"
                    btn.result_time = st
                    renpy.sound.play(QTE_SFX_MISS, channel="sound")

                if btn.result is None:
                    ring_color = "#4ade80" if in_window else "#facc15"
                    rs = int(ring_sz)
                    ring_r = renpy.Render(rs, rs)
                    ring_r.canvas().circle(ring_color, (rs // 2, rs // 2), rs // 2, 3)
                    r.blit(ring_r, (cx - rs // 2, cy - rs // 2))

                if btn.result == "hit":
                    fill_color   = "#4ade80"
                    border_color = "#22c55e"
                    icon_color   = "#ffffff"
                elif btn.result == "miss":
                    fill_color   = "#f87171"
                    border_color = "#ef4444"
                    icon_color   = "#ffffff"
                else:
                    fill_color   = "#3b3b5c"
                    border_color = "#ffffff"
                    icon_color   = "#ffffff"

                btn_r = renpy.Render(bs, bs)
                btn_c = btn_r.canvas()
                btn_c.circle(fill_color, (bs // 2, bs // 2), bs // 2)
                btn_c.circle(border_color, (bs // 2, bs // 2), bs // 2, 3)
                r.blit(btn_r, (cx - bs // 2, cy - bs // 2))

                isz       = QTE_ICON_SIZE
                icon_d    = Transform(QTE_ICON_IMG, xysize=(isz, isz), fit="contain")
                icon_surf = renpy.render(icon_d, isz, isz, st, at)
                r.blit(icon_surf, (cx - isz // 2, cy - isz // 2))

                if btn.result is not None and btn.result_time is not None:
                    age = st - btn.result_time
                    if age < QTE_HOLD_TIME:
                        label     = QTE_TEXT_HIT  if btn.result == "hit" else QTE_TEXT_MISS
                        txt_color = QTE_COLOR_HIT if btn.result == "hit" else QTE_COLOR_MISS
                        txt_d     = Text(label, size=QTE_TEXT_SIZE, bold=True, color=txt_color,
                                        font=QTE_FONT, outlines=[(3, "#000000", 0, 0)])
                        tw, th     = txt_d.size()
                        txt_surf   = renpy.render(txt_d, tw, th, st, at)
                        r.blit(txt_surf, (cx - tw // 2, cy - bs // 2 - th - 12))
                        need_redraw = True
                    else:
                        btn.visible = False
                        need_redraw = True

                if btn.result is None:
                    need_redraw = True

            if need_redraw:
                renpy.redraw(self, 0)
            elif self.all_done():
                latest_result_time = max(
                    b.result_time for b in self.buttons if b.result_time is not None
                )
                if st - latest_result_time >= QTE_HOLD_TIME:
                    renpy.restart_interaction()

            return r

        def event(self, ev, x, y, st):
            import pygame
            if ev.type != pygame.MOUSEBUTTONDOWN or ev.button != 1:
                raise renpy.IgnoreEvent()

            if self.global_start is None:
                raise renpy.IgnoreEvent()

            for btn in self.buttons:
                if btn.result is not None:
                    continue
                if btn.start_time is None:
                    continue
                if not btn.visible:
                    continue

                dist = ((x - btn.cx) ** 2 + (y - btn.cy) ** 2) ** 0.5
                if dist > QTE_BUTTON_SIZE // 2 + 10:
                    continue

                ring_sz = btn.ring_size(st)
                if ring_sz <= QTE_BUTTON_SIZE + QTE_HIT_WINDOW:
                    btn.result = "hit"
                    renpy.sound.play(QTE_SFX_HIT, channel="sound")
                else:
                    btn.result = "miss"
                    renpy.sound.play(QTE_SFX_MISS, channel="sound")

                btn.result_time = st
                renpy.redraw(self, 0)
                return None

            raise renpy.IgnoreEvent()

        def visit(self):
            return []


    def make_qte_buttons(screen_w, screen_h, count=3):
        margin   = QTE_MARGIN
        min_dist = 200

        cx_min = screen_w  // 6
        cx_max = screen_w  * 5 // 6
        cy_min = 120
        cy_max = screen_h  // 3

        positions = []
        for _ in range(count):
            for attempt in range(100):
                cx = random.randint(cx_min, cx_max)
                cy = random.randint(cy_min, cy_max)
                too_close = any(
                    ((cx - px) ** 2 + (cy - py) ** 2) ** 0.5 < min_dist
                    for px, py in positions
                )
                if not too_close:
                    break
            positions.append((cx, cy))

        buttons = []
        for i, (cx, cy) in enumerate(positions):
            delay = i * random.uniform(0.3, 0.5)
            buttons.append(QTEButton(cx, cy, delay))

        return buttons


screen qte_screen(qte_multi):
    add qte_multi
    timer 0.05 repeat True action If(
        qte_multi.all_done(),
        true=Return(qte_multi.results())
    )


transform wiggle:
    zoom 1.05
    linear 0.5 xpos -5 ypos -10
    linear 0.5 xpos -10 ypos -5
    linear 0.5 xpos -8 ypos -6
    linear 0.5 xpos -5 ypos -10
    repeat