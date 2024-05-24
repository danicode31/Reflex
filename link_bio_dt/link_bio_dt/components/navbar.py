import reflex as rx
import link_bio_dt.styles.color as color
import link_bio_dt.styles.styles as styles


def navbar() -> rx.Component:
    return (
        rx.flex(
            rx.vstack(
                rx.image(
                    src="/cover_band.jpg",
                    width=styles.MAX_WIDTH,
                    alt="presentacion",
                ),
            #     rx.hstack(
                  
            #     ),
            #     rx.menu.root(
            #         rx.menu.trigger(
            #             rx.button("Menu",justify= 'center'
            #                       ),
                        
            #         ),
            #         rx.menu.content(
            #             rx.menu.item("item 1"),
            #             rx.menu.separator(),
            #             rx.menu.item("Item 2"),
            #             rx.menu.item("Item 3"),
            #             width="10rem",
            #         ),
            #     ),
            #     # top="0px",
            #     # padding="1em",
            #     # height="4em",
            #     # width="100%",
            #     # #z_index="5",
            # ),
            
        ),
            align_items="center",
            justify_content="center",
            bg=color.Color.BGACCORDION.value,
    )
    )
