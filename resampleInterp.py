            window_size =  "24H" 
            sampling_interval=  "15S"
            newdate_range = pd.date_range(Min_Tstamp,Max_Tstamp, freq= sampling_interval) 
            df = df.reindex(self.newdaterange).interpolate(method='linear').resample(window_size).mean().bfill()
            
            
       
   
      
        
      
      
