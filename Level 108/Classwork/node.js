function cache(func) {
    const cachedData = {}
    
    function inner (...args) {
        if ((Object.keys(cachedData)).includes({...args} )) {
            return cachedData[{...args}]
        }
        
        const result = func(...args)
        
        cachedData[{...args}] = result
        
        return result
    }
    
    return inner
}