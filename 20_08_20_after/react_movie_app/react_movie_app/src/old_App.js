import React from 'react';
import PropTypes from "prop-types";

// import Potato from "./Potato";
//
// function Food(props) {
 // console.log(props.fav);
 // return <h2>I love {props.fav}. </h2>;
 // }
// props로 fav 등 다양한 것을 가져올 수 있음!
// component는 대문자 ! / props는 component에 넣는 것들!
// function Food({fav}) {
  // console.log(fav);
  // return <h2>I love {fav}. </h2>;
// }


const foodILike = [
  {
    id: 1,
    name: "Kimchi",
    image:
      "http://aeriskitchen.com/wp-content/uploads/2008/09/kimchi_bokkeumbap_02-.jpg",
    rating: 4.8
  },
  {
    id: 2,
    name: "Samgyeopsal",
    image:
      "https://3.bp.blogspot.com/-hKwIBxIVcQw/WfsewX3fhJI/AAAAAAAAALk/yHxnxFXcfx4ZKSfHS_RQNKjw3bAC03AnACLcBGAs/s400/DSC07624.jpg",
    rating: 4.2
  },
  {
    id: 3,
    name: "Bibimbap",
    image:
      "http://cdn-image.myrecipes.com/sites/default/files/styles/4_3_horizontal_-_1200x900/public/image/recipes/ck/12/03/bibimbop-ck-x.jpg?itok=RoXlp6Xb",
    rating: 3.9
  },
  {
    id: 4,
    name: "Doncasu",
    image:
      "https://s3-media3.fl.yelpcdn.com/bphoto/7F9eTTQ_yxaWIRytAu5feA/ls.jpg",
    rating: 4.91
  },
  {
    id: 5,
    name: "Kimbap",
    image:
      "http://cdn2.koreanbapsang.com/wp-content/uploads/2012/05/DSC_1238r-e1454170512295.jpg"
  }
];
function Food({ name, picture, rating }) {
  return (
    <div>
      <h2>I like {name}</h2>
      <h2>{rating}/5.0</h2>
      <img src= {picture} alt={name} />
    </div>
  );
};
Food.propTypes = {
  name: PropTypes.string.isRequired,
  rating : PropTypes.number,
  picture : PropTypes.string.isRequired
}

// function renderFood(dish){
  // console.log(dish);
  // return <Food Key = {dish.id} name = {dish.name} picture={dish.image}/>
// }
function App() {
  return (
    // <Food fav = "kimchi"/>
    // <Food fav = "chicken"/>
    // <Food fav = "love"/>
    // <Food fav = "ramen"/>
    <div>
      {foodILike.map(dish => (
        <Food key={dish.id} name={dish.name} picture={dish.image} rating={dish.rating} />
      ))}
    </div>
    // <div>
    // {foodILike.map(renderFood)}
    // </div>
  );
}
export default App;
