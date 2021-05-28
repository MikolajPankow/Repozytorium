import './App.css'
import React, {Component} from "react"

class App extends Component {
  constructor() {
    super()
    this.state = {
      loading: false,
      jedzenie: {}
    }
  }

  componentDidMount() {
    this.setState({loading: true})
    fetch("http://127.0.0.1:8000/posilki/1/")
      .then(response => response.json())
      .then(data => {
        this.setState({
          loading: false,
          jedzenie: data
        })
      })
  }

  render() {
    const nazwa = this.state.loading ? "loading..." : this.state.jedzenie.nazwa
    const rodzaj = this.state.loading ? "loading..." : this.state.jedzenie.rodzaj
    return(
      <div>
        <p>Nazwa: {nazwa}</p>
        <p>Rodzaj: {rodzaj}</p>
      </div>
    )
  }
}

export default App
