import React,{Component} from 'react';

import Post from './Post/Post';
import axios from '../MyAxios/MyAxios';
import Loader from '../UI/Loader/Loader';

class Posts extends Component{
    state = {
        posts:[],
        error:'',
        loading:true
    }

    componentDidMount(){
        axios.get('api/posts').then(response=>{
            this.setState({posts:response.data,
                           error:'',
                           loading:false
                          })
        }).catch(error=>{
            this.setState({error:error.message})
        })
    }

    render(){
        const loading = <div className="col-12 text-center mt-5"><Loader /></div>
        let view ;
        if (this.state.error){
            view = <div>
                    <h3 className="text-center mt-5">
                        {this.state.error}
                    </h3>
                   </div>    
        }
        else if(this.state.posts){
            view = this.state.posts.map((post)=>{
                return <Post details={post} key={post.id}/>  
            })         
        }
        return (
        <div className="row p-5">
            {this.state.loading ? loading:''}
            {view}

        </div>)
    }
}


export default Posts;