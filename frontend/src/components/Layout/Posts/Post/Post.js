import React from 'react';
import classes from './Post.module.css';
import {Link} from 'react-router-dom';
import reactStringReplace from 'react-string-replace';



const post = (props) => {
    const newContent = reactStringReplace(props.details.content,
                                          /(#[a-z\d][\w-]+)/ig,
                                          (match, i) => (
                                       <Link key={i} className={[classes.Link,classes.Tag].join(' ')} to={'/'+ match}>
                                           {match}
                                       </Link> )
                        ); 
        
        return (
        <div className="col-12 mt-4">
            <div className={[classes.Card, "card"].join(' ')}>
                <div className="card-body">
                    <div className={classes.Grid}>
                        <div>
                            
                            <img className={[classes.Avatar,'text-left'].join(' ')} 
                                 src={props.details.user.image} />
                        </div>
                        
                        <div className={classes.Body}>
                            <div>
                                <Link to={`/` + props.details.user.slug} className={classes.Link}>
                                        {props.details.user.username}
                                </Link>
                                <br />
                                {newContent}
                            </div>
                            <div className={classes.Date}>
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