import numpy as np


DATA_SAMPE_FORMAT = {
    1 : "",
    2 : "i4",
    3 : "i2",
    4 : "f4",
    5 : "f4",
    6 : "f8",
    7 : ""
}

BIG_BINARY_HEADER_REV2 = np.dtype([
    ("job_id", ">i4"),                # 3201-3204
    ("line_number", ">i4"),           # 3205-3208
    ("reel_number", ">i4"),           # 3209-3212
    ("num_traces", ">i2"),            # 3213-3214
    ("num_aux_traces", ">i2"),        # 3215-3216
    ("sample_interval", ">i2"),       # 3217-3218
    ("sample_interval_original", ">i2"),  # 3219-3220
    ("samples_per_trace", ">i2"),     # 3221-3222
    ("samples_per_trace_original", ">i2"), # 3223-3224
    ("data_sample_format", ">i2"),    # 3225-3226
    ("ensemble_fold", ">i2"),         # 3227-3228
    ("trace_sorting", ">i2"),         # 3229-3230
    ("vertical_sum", ">i2"),          # 3231-3232
    ("sweep_freq_start", ">i2"),      # 3233-3234
    ("sweep_freq_end", ">i2"),        # 3235-3236
    ("sweep_length", ">i2"),          # 3237-3238
    ("sweep_type", ">i2"),            # 3239-3240
    ("trace_num_sweep", ">i2"),       # 3241-3242
    ("sweep_taper_start", ">i2"),     # 3243-3244
    ("sweep_taper_end", ">i2"),       # 3245-3246
    ("taper_type", ">i2"),            # 3247-3248
    ("correlated", ">i2"),            # 3249-3250
    ("binary_gain_recovered", ">i2"), # 3251-3252
    ("amplitude_recovery_method", ">i2"), # 3253-3254
    ("measurement_system", ">i2"),    # 3255-3256
    ("impulse_polarity", ">i2"),      # 3257-3258
    ("vibratory_polarity", ">i2"),    # 3259-3260
    ("ext_num_traces", ">i4"),        # 3261-3264
    ("ext_num_aux_traces", ">i4"),    # 3265-3268
    ("ext_samples_per_trace", ">i4"), # 3269-3272
    ("ext_sample_interval", np.float64), # 3273-3280 (8 bytes)
    ("ext_sample_interval_orig", np.float64), # 3281-3288 (8 bytes)
    ("ext_samples_per_trace_orig", ">i4"), # 3289-3292
    ("ext_ensemble_fold", ">i4"),     # 3293-3296
    ("byte_order_constant", ">i4"),   # 3297-3300 (0x01020304)
    ("reserved1", "V200"),
    ("rev_num", ">i2"),               # 3501-3502 (major/minor)
    ("fixed_length_flag", ">i2"),     # 3503-3504
    ("num_ext_headers", ">i2"),       # 3505-3506
    ("max_num_add_trace_headers", ">i2"), # 3507-3508
    ("survey_type", ">i2"),           # 3509-3510
    ("time_basis_code", ">i2"),       # 3511-3512
    ("num_traces_file", ">i8"),      # 3513-3520 (8 bytes)
    ("offset_first_trace", ">i8"),   # 3521-3528 (8 bytes)
    ("num_trailer_stanzas", ">i4"),   # 3529-3532
    ("reserved2", "V68"),
])


LITTLE_BINARY_HEADER_REV2 = np.dtype([
    ("job_id", "<i4"),                # 3201-3204
    ("line_number", "<i4"),           # 3205-3208
    ("reel_number", "<i4"),           # 3209-3212
    ("num_traces", "<i2"),            # 3213-3214
    ("num_aux_traces", "<i2"),        # 3215-3216
    ("sample_interval", "<i2"),       # 3217-3218
    ("sample_interval_original", "<i2"),  # 3219-3220
    ("samples_per_trace", "<i2"),     # 3221-3222
    ("samples_per_trace_original", "<i2"), # 3223-3224
    ("data_sample_format", "<i2"),    # 3225-3226
    ("ensemble_fold", "<i2"),         # 3227-3228
    ("trace_sorting", "<i2"),         # 3229-3230
    ("vertical_sum", "<i2"),          # 3231-3232
    ("sweep_freq_start", "<i2"),      # 3233-3234
    ("sweep_freq_end", "<i2"),        # 3235-3236
    ("sweep_length", "<i2"),          # 3237-3238
    ("sweep_type", "<i2"),            # 3239-3240
    ("trace_num_sweep", "<i2"),       # 3241-3242
    ("sweep_taper_start", "<i2"),     # 3243-3244
    ("sweep_taper_end", "<i2"),       # 3245-3246
    ("taper_type", "<i2"),            # 3247-3248
    ("correlated", "<i2"),            # 3249-3250
    ("binary_gain_recovered", "<i2"), # 3251-3252
    ("amplitude_recovery_method", "<i2"), # 3253-3254
    ("measurement_system", "<i2"),    # 3255-3256
    ("impulse_polarity", "<i2"),      # 3257-3258
    ("vibratory_polarity", "<i2"),    # 3259-3260
    ("ext_num_traces", "<i4"),        # 3261-3264
    ("ext_num_aux_traces", "<i4"),    # 3265-3268
    ("ext_samples_per_trace", "<i4"), # 3269-3272
    ("ext_sample_interval", np.float64), # 3273-3280 (8 bytes)
    ("ext_sample_interval_orig", np.float64), # 3281-3288 (8 bytes)
    ("ext_samples_per_trace_orig", "<i4"), # 3289-3292
    ("ext_ensemble_fold", "<i4"),     # 3293-3296
    ("byte_order_constant", "<i4"),   # 3297-3300 (0x01020304)
    ("reserved1", "V200"),
    ("rev_num", "<i2"),               # 3501-3502 (major/minor)
    ("fixed_length_flag", "<i2"),     # 3503-3504
    ("num_ext_headers", "<i2"),       # 3505-3506
    ("max_num_add_trace_headers", "<i2"), # 3507-3508
    ("survey_type", "<i2"),           # 3509-3510
    ("time_basis_code", "<i2"),       # 3511-3512
    ("num_traces_file", "<u8"),      # 3513-3520 (8 bytes)
    ("offset_first_trace", "<u8"),   # 3521-3528 (8 bytes)
    ("num_trailer_stanzas", "<i4"),   # 3529-3532
    ("reserved2", "V68"),
])

BIG_TRACE_HEADER = np.dtype([

])

LITTLE_TRACE_HEADER = np.dtype([
    
])

