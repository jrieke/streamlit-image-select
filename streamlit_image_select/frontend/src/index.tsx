import { Streamlit, RenderData } from "streamlit-component-lib"

const labelDiv = document.body.appendChild(document.createElement("label"))
const label = labelDiv.appendChild(document.createTextNode(""))
const imagesDiv = document.body.appendChild(document.createElement("div"))
imagesDiv.classList.add("image-picker")

/**
 * The component's render function. This will be called immediately after
 * the component is initially loaded, and then again every time the
 * component gets new data from Python.
 */
function onRender(event: Event): void {
  // Get the RenderData from the event
  const data = (event as CustomEvent<RenderData>).detail

  if (data.theme) {
    labelDiv.style.font = data.theme.font
    labelDiv.style.color = data.theme.textColor
    if (data.theme.base === "dark") {
      document.body.querySelectorAll(".option").forEach((el) => {
        el.classList.add("dark")
      })
    } else {
      document.body.querySelectorAll(".option").forEach((el) => {
        el.classList.remove("dark")
      })
    }
  }

  label.textContent = data.args["label"]
  let images = data.args["images"]

  if (imagesDiv.childNodes.length === 0) {
    images.forEach((image: string, i: number) => {
      let imgDiv = imagesDiv.appendChild(document.createElement("div"))
      imgDiv.classList.add("option")

      let img = imgDiv.appendChild(document.createElement("img"))
      img.classList.add("thumbnail")
      img.src = image

      if (i === 0) {
        imgDiv.classList.add("selected")
        img.classList.add("selected")
      }

      img.onclick = function () {
        imagesDiv.querySelectorAll(".selected").forEach((el) => {
          el.classList.remove("selected")
        })
        Streamlit.setComponentValue(i)
        imgDiv.classList.add("selected")
        img.classList.add("selected")
      }
    })
  }

  // We tell Streamlit to update our frameHeight after each render event, in
  // case it has changed. (This isn't strictly necessary for the example
  // because our height stays fixed, but this is a low-cost function, so
  // there's no harm in doing it redundantly.)
  Streamlit.setFrameHeight()
}

// Attach our `onRender` handler to Streamlit's render event.
Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)

// Tell Streamlit we're ready to start receiving data. We won't get our
// first RENDER_EVENT until we call this function.
Streamlit.setComponentReady()

// Finally, tell Streamlit to update our initial height. We omit the
// `height` parameter here to have it default to our scrollHeight.
Streamlit.setFrameHeight()
