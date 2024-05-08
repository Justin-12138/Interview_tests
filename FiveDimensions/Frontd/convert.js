import React, { useState, useEffect } from 'react';

class MyClassComponent extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            count: 0
        };
    }

    componentDidMount() {
        console.log('Component did mount');
    }

    componentDidUpdate() {
        console.log('Component did update');
    }

    componentWillUnmount() {
        console.log('Component will unmount');
    }

    handleClick = () => {
        this.setState({ count: this.state.count + 1 });
    }

    render() {
        return (
            <div>
                <p>You clicked {this.state.count} times</p>
                <button onClick={this.handleClick}>
                    Click me
                </button>
            </div>
        );
    }
}


function MyFunctionComponent() {
    const [count, setCount] = useState(0);

    useEffect(() => {
        console.log('Equivalent to componentDidMount and componentDidUpdate');
        return () => {
            console.log('Equivalent to componentWillUnmount');
        };
    }, [count]);

    const handleClick = () => {
        setCount(count + 1);
    }

    return (
        <div>
            <p>You clicked {count} times</p>
            <button onClick={handleClick}>
                Click me
            </button>
        </div>
    );
}
