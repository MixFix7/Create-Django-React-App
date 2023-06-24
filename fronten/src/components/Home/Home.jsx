import React from 'react'
import { useLoaderData } from 'react-router-dom'

export const Home = () => {
    const name = useLoaderData()
    console.log(name)

  return (
    <div>
        <h1>Welcome, {name.map((name) => (
            name.name
        ))}</h1>
        <h2>Let's start building a new Website?</h2>
    </div>
  )
}
