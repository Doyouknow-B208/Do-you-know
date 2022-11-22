const BE = 'https://j7b208.p.ssafy.io/api/'
const BE2 = 'https://j7b208.p.ssafy.io/api2/'


// DYKC API
const DYKC = 'dykclub/'

// DataLab API
const DataLab = 'keyword/'


export default{
  // DYKC
  dykc: {
    DYKC: (keyword) => BE + DYKC + `${keyword}/`,
    twitter: (name) => BE + DYKC + DataLab + `${name}/`,
  },

  // DataLab
  datalab: {
    relatedkeyword : (keyword) => BE2 + "pytrend/relativerisingkeyword/" + keyword,
  }
}
