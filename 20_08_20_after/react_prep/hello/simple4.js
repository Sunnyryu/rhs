class Container extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 0
    };
  }

  render() {
    return /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement(LikeButton, null), /*#__PURE__*/React.createElement("div", {
      style: "{{marginTop:20}}"
    }, /*#__PURE__*/React.createElement("span", null, "\uD604\uC7AC\uCE74\uC6B4\uD2B8:"), /*#__PURE__*/React.createElement("span", null, this.state.count), /*#__PURE__*/React.createElement("button", {
      onClick: () => this.setState({
        count: this.state.count + 1
      })
    }, "\uC99D\uAC00"), /*#__PURE__*/React.createElement("button", {
      onClick: () => this.setState({
        count: this.state.count - 1
      })
    }, "\uAC10\uC18C")));
  }

}