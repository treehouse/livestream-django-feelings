import React from 'react';
import ReactDOM from 'react-dom';
import 'whatwg-fetch';

import { RecentThoughts } from './recent_thoughts';
import { ThoughtForm } from './thought_form';

class RootElement extends React.Component {
    // componentDidMount() {
    //     this.user = fetch(
    //         '/api/users.json', {
    //             credentials: 'same-origin'
    //         }
    //     ).then(function(response) {
    //         return response.json()
    //     }).then(function(json) {
    //        console.log(json);
    //     });
    // };

    render() {
        return (
            <div className="row">
                <div className="col-md-6">
                    <RecentThoughts/>
                </div>
                <div className="col-md-6">
                    <ThoughtForm/>
                </div>
            </div>
        )
    }
}

ReactDOM.render(
    <RootElement/>,
    document.getElementById('react-app')
);

