class Cat {
  constructor(name){
    this.name = name
  }

  sound(adj){
    console.log(`${this.name} meows ${adj}`)
  }
}
class Dog {
  constructor(name){
    this.name = name
  }

  sound(adj){
    console.log(`${this.name} barks ${adj}`)
  }
}

const cat = new Cat('mittens')
const dog = new Dog('Fido')

dog.sound.apply(cat, ['loudly']);
dog.sound.call(cat, 'loudly');