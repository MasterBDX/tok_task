import React from 'react';
import {NavLink} from 'react-router-dom';

import classes from './Nav.module.css'

const navbar = () => {
    return (
        <nav  className={[classes.Navbar,"navbar","navbar-expand-lg","navbar-dark"].join(' ')}>
            <div  className="container-fluid">
                <a  className="navbar-brand" href="/">Tok Task</a>
                <button  className={[classes.Button,"navbar-toggler"].join(' ')} type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span  className="navbar-toggler-icon"></span>
                </button>
                <div  className="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul  className="navbar-nav mb-2 mb-lg-0">
                        <li  className="nav-item">
                            <NavLink className="nav-link" to="/" activeClassName={classes.Active}>Home </NavLink>
                        </li>
                        <li  className="nav-item">
                             <NavLink className="nav-link" to="/posts" activeClassName={classes.Active}>News</NavLink>
                        </li>
                        <li  className="nav-item">
                             <NavLink className="nav-link" to="/posts" activeClassName={classes.Active}>
                                 <div className={classes.ICON_CON}>
                                <span className="d-lg-none d-inline">New Post</span>
                                 <span className="d-lg-inline d-none">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-plus-circle" viewBox="0 0 16 16">
                                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
                                        <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"/>
                                    </svg>
                                </span>
                                 </div>
                            </NavLink>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    )
}


export default navbar;