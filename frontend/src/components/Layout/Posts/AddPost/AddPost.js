import React,{Component} from 'react';

import axios from '../../MyAxios/MyAxios';

import classes from './AddPost.module.css';

class AddPost extends Component {
    state = {data:null}

    PostAddHandler(event){
        event.preventDefault();
        axios.post('')
    }

    AddOnChangeHandler(event){
        event.preventDefault();
        const value = event.target.value
        if (value.length > 220){
            alert('The post is too long')
        }
        else{
            this.setState({data:value})
        }
    }

    render (){
        return <div className="p-5 text-center">
                    <form onSubmit={this.PostAddHandler} className="" 
                          action="">
                        <div className="mb-3">
                            <textarea onChange={this.AddOnChangeHandler} className={[classes.TextArea].join(' ')}
                                      maxLength="220"
                            >

                            </textarea>
                        </div>
                        
                        <button className={classes.Button} type="submit">
                            Add
                        </button>
                    </form>
                </div>
    }
} 


export default AddPost;