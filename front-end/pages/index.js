import Head from 'next/head'
import { useState } from 'react'


export default function Home() {
  const [showImage, setShowImage] = useState(false);
  const [imgUrl, setImgUrl] = useState();

  const SearchBar = () => {
  
    return (
      <div>
        <input type="text" onKeyDown={onEnter} />
      </div>
    )
  }

  const onEnter = async event => {

    if (event.key == 'Enter') {
      const res = await fetch(
        `http://localhost:8000/api/v1/world-clouds?keyword=${event.target.value}`
      )
  
      const result = await res.json()
      setImgUrl(result.image)
      setShowImage(true)
    }
  }

  return (
    <div className="container">
      <Head>
        <title>World Cloud Project</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main>
        <h1 className="title">
          Word Cloud Project
        </h1>

        <p className="description">
          Get started here <SearchBar />
        </p>

        { showImage &&
          <img src={imgUrl} />
        }
      </main>
    </div>
  )
}
