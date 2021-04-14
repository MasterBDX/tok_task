import React from 'react';
import { Route,Switch } from 'react-router-dom';
import Posts from '../../Posts/Posts';
import AddPost from '../../Posts/AddPost/AddPost';

const MainBox = () => {
    return (<div>
        <Switch>
            <Route path='/' exact  render={()=>(<h2 className="text-center mt-5">Home Page</h2>)} />        
            <Route path='/posts' exact component={Posts} />
            <Route path='/posts/add' component={AddPost} />
            <Route path='/results' render={()=>(<h2 className="text-center mt-5">Results Page</h2>)}/>
        </Switch>
    </div>)
}

export default MainBox;