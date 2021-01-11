import defaultAxios from "axios";
import { useEffect, useState } from "react";

const useAxios = (opts, axiosInstance = defaultAxios) => {
  const [state, setState] = useState({
    loading: true,
    error: null,
    data: null
  });
  //console.log(state)
  const [trigger, setTrigger] = useState(0);
  
//   if (!opts.url) {
    // return;
//   }
  const refetch = () => {
    setState({
      ...state,
      loading: true
    });
    setTrigger(Date.now());
  };
  useEffect(() => {
    axiosInstance(opts).then((data) => {
      setState({
        ...state,
        loading: false,
        data
      });
      //console.log(data);
    });
  }, [trigger]);
  //console.log(trigger)
  return { ...state, refetch };
};

export default useAxios;
