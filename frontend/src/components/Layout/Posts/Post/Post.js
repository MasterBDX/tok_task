import React from 'react';
import classes from './Post.module.css';
import {Link} from 'react-router-dom';
import reactStringReplace from 'react-string-replace';



const post = (props) => {
    const newContent = reactStringReplace(props.details.content,
                                          /(#[a-z\d][\w-]+)/ig,
                                          (match, i) => (
                                       <Link className={[classes.Link,classes.Tag].join(' ')} to={'/'+ match}>
                                           {match}
                                       </Link> )
                        ); 
        console.log(newContent)
        return (
        <div className="col-12 mt-4">
            <div className={[classes.Card, "card"].join(' ')}>
                <div className="card-body">
                    <div className={classes.Grid}>
                        <div>
                            <img className={classes.Avatar} src="https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8dXNlcnxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&w=1000&q=80" />
                        </div>
                        
                        <div className={classes.Body}>
                            <div>
                                <Link to={`/` + props.details.user.slug} className={classes.Link}>
                                        {props.details.user.username}
                                </Link>
                                <br />
                                {newContent}
                                {/* <a href="#" className={[classes.Link,classes.Tag].join(' ')}>#tag</a>
                                <a href="#" className={[classes.Link,classes.Tag].join(' ')}>#tag</a>
                                <a href="#" className={[classes.Link,classes.Tag].join(' ')}>#tag</a>
                                <a href="#" className={[classes.Link,classes.Tag].join(' ')}>#tag</a> */}
                            </div>
                            <div>
                                {props.details.timestamp}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}


export default post;