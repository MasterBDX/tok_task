import React from 'react';

import MainBox from './MainBox/MainBox';

const Main = () =>{
    return (<div className="row">
                <div className="col-md-4">
                    <h1 className="text-center mt-5">
                            Sub Box
                    </h1>
                </div>
                <div className="col-md-8">
                    <MainBox />
                </div>
            </div>)
}

export default Main;