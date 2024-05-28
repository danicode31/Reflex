import reflex as rx
from link_bio_dt.styles import styles



def link_button(image: str, url: str, alt: str, size="2", variant="solid", radius="small") -> rx.Component:
  """
  Creates a link button with an image and hover effect.

  Args:
      image: Path to the image source.
      url: URL of the link.
      alt: Alternative text for the image.
      size: Button size (default: "2").
      variant: Button variant (default: "solid").
      radius: Button corner radius (default: "small").

  Returns:
      rx.Component representing the link button.
  """

  return rx.link(
      rx.button(
          rx.image(src=image, width=styles.Spacing.LARGE.value, height=styles.Spacing.LARGE.value, alt=alt),
          color_scheme="gold",
          size=size,
          variant=variant,
          radius=radius,
          opacity=0.6,
          _hover={"opacity": 1},
      ),
      href=url,
      is_external=True,
      text_decoration="none",
  )