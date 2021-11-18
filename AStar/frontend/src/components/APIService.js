export default class APIService {
    // Insert an article
  
    static insertArticle(body) {
      console.log("im in insertarticle");
      return fetch(`https://astarchooser.herokuapp.com/user/login`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(body)
      })
        .then((response) => response.json())
        .then(data => this.setState({userID: data.id}))
        .catch((error) => console.log(error));
    }

    static postQuery(query) {
      console.log("im in postQuery");
      return fetch(`https://astarchooser.herokuapp.com/add`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        query: JSON.stringify(query)
      })
        .then((response) => response.json())
        .catch((error) => console.log(error));
    }

    
  }
  