import tkinter as tk
from tkinter import ttk
from section_parameters.SectionParametersE6 import SectionParametersE6
from app.StyleConfiguration import StyleConfiguration
from app.DirectoryGenerator import DirectoryGenerator
from testsite_data.TestsiteDataE6 import TestsiteDataE6
from testsite_data.TestsiteDataRoros import TestsiteDataRoros
from testsite_data.TestsiteDataFinland import TestsiteDataFinland
from testsite_data.TestsiteDataSweden import TestsiteDataSweden

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Plot figures')

        # FRAME LAYOUT:
        # self.main_frame (top)
            # testsite_year_plot_options_frame (top)
                # testsite_year_frame (left)
                # plot_options_frame (left)

        # Sample data:
        self.E6_data = TestsiteDataE6()
        self.E6_years = [sample['year_name'] for sample in self.E6_data.year_list]
        self.Roros_data = TestsiteDataRoros()
        self.Roros_years = [sample['year_name'] for sample in self.Roros_data.year_list]
        self.Finland_data = TestsiteDataFinland()
        self.Finland_years = [sample['year_name'] for sample in self.Finland_data.year_list]
        self.Sweden_data = TestsiteDataSweden()
        self.Sweden_years = [sample['year_name'] for sample in self.Sweden_data.year_list]
        self.testsite_object_list = [self.E6_data,
                                     self.Roros_data,
                                     self.Finland_data,
                                     self.Sweden_data]
        self.active_testsite = self.E6_data

        # Directory generator
        dir_generator = DirectoryGenerator()
        dir_generator.generate_directories(self.E6_data)

        # Adding main frame:
        self.main_frame = ttk.Frame(self, style='Standard.TFrame', padding=10)
        self.main_frame.grid(row=0, column=0)

        # Adding section frames:
        self.testsite_year_plot_options_frame = ttk.Frame(self.main_frame, style='Standard.TFrame')
        self.testsite_year_plot_options_frame.pack(side='top', fill='x')
        self.testsite_year_frame = ttk.Frame(self.testsite_year_plot_options_frame, style='Standard.TFrame')
        self.testsite_year_frame.pack(side='left', fill='y')
        self.plot_options_frame = ttk.Frame(self.testsite_year_plot_options_frame, style='Standard.TFrame')
        self.plot_options_frame.pack(side='left', fill='both', expand=True, padx=(10, 0))

        self.plot_control_frame = ttk.Frame(self.main_frame, style='Standard.TFrame')
        self.plot_control_frame.pack(side='top', fill='x')

        # Testsite section widgets:
        self.testsite_frame = ttk.Frame(self.testsite_year_frame, style='Standard.TFrame')
        self.testsite_frame.pack(side='top', fill='x')
        self.testsite_label_frame = ttk.Frame(self.testsite_frame, style='DarkFrame.TFrame')
        self.testsite_label_frame.pack(side='top', fill='x')
        self.testsite_label = ttk.Label(self.testsite_label_frame,
                                        text='Testsite selection:',
                                        style='ExtraLargeLabel.TLabel')
        self.testsite_label.pack(side='left', padx=(10, 0), pady=(5, 5))

        self.testsite_var = tk.StringVar(value=self.E6_data.testsite_dir['name'])
            # values: e6, roros, finland, sweden

        self.testsite_E6_radiobutton_frame = ttk.Frame(self.testsite_frame, style='Standard.TFrame')
        self.testsite_E6_radiobutton_frame.pack(side='top', fill='x')
        self.testsite_E6_radiobutton = ttk.Radiobutton(self.testsite_E6_radiobutton_frame,
                                                       style='Standard.TRadiobutton',
                                                       value=self.E6_data.testsite_dir['name'],
                                                       variable=self.testsite_var,
                                                       takefocus=False,
                                                       command=self.update_combobox)
        self.testsite_E6_radiobutton.pack(side='left', pady=(10, 0), padx=(20, 0))
        self.testsite_E6_radiobutton_text = ttk.Label(self.testsite_E6_radiobutton_frame,
                                                      style='LeftAligned.TLabel',
                                                      text='Trondheim, E6')
        self.testsite_E6_radiobutton_text.pack(side='left', padx=(5, 5), pady=(10, 0))

        self.testsite_Roros_radiobutton_frame = ttk.Frame(self.testsite_frame, style='Standard.TFrame')
        self.testsite_Roros_radiobutton_frame.pack(side='top', fill='x')
        self.testsite_Roros_radiobutton = ttk.Radiobutton(self.testsite_Roros_radiobutton_frame,
                                                          style='Standard.TRadiobutton',
                                                          value=self.Roros_data.testsite_dir['name'],
                                                          variable=self.testsite_var,
                                                          takefocus=False,
                                                          command=self.update_combobox)
        self.testsite_Roros_radiobutton.pack(side='left', pady=(10, 0), padx=(20, 0))
        self.testsite_Roros_radiobutton_text = ttk.Label(self.testsite_Roros_radiobutton_frame,
                                                         style='LeftAligned.TLabel',
                                                         text='Røros')
        self.testsite_Roros_radiobutton_text.pack(side='left', padx=(5, 5), pady=(10, 0))

        self.testsite_Finland_radiobutton_frame = ttk.Frame(self.testsite_frame, style='Standard.TFrame')
        self.testsite_Finland_radiobutton_frame.pack(side='top', fill='x')
        self.testsite_Finland_radiobutton = ttk.Radiobutton(self.testsite_Finland_radiobutton_frame,
                                                            style='Standard.TRadiobutton',
                                                            value=self.Finland_data.testsite_dir['name'],
                                                            variable=self.testsite_var,
                                                            takefocus=False,
                                                            command=self.update_combobox)
        self.testsite_Finland_radiobutton.pack(side='left', pady=(10, 0), padx=(20, 0))
        self.testsite_Finland_radiobutton_text = ttk.Label(self.testsite_Finland_radiobutton_frame,
                                                           style='LeftAligned.TLabel',
                                                           text='Finland')
        self.testsite_Finland_radiobutton_text.pack(side='left', padx=(5, 5), pady=(10, 0))

        self.testsite_Sweden_radiobutton_frame = ttk.Frame(self.testsite_frame, style='Standard.TFrame')
        self.testsite_Sweden_radiobutton_frame.pack(side='top', fill='x')
        self.testsite_Sweden_radiobutton = ttk.Radiobutton(self.testsite_Sweden_radiobutton_frame,
                                                           style='Standard.TRadiobutton',
                                                           value=self.Sweden_data.testsite_dir['name'],
                                                           variable=self.testsite_var,
                                                           takefocus=False,
                                                           command=self.update_combobox)
        self.testsite_Sweden_radiobutton.pack(side='left', pady=(10, 0), padx=(20, 0))
        self.testsite_Sweden_radiobutton_text = ttk.Label(self.testsite_Sweden_radiobutton_frame,
                                                          style='LeftAligned.TLabel',
                                                          text='Sweden')
        self.testsite_Sweden_radiobutton_text.pack(side='left', padx=(5, 5), pady=(10, 0))

        # Year selection widgets:
        self.year_frame = ttk.Frame(self.testsite_year_frame, style='Standard.TFrame')
        self.year_frame.pack(side='top', fill='x', pady=(20, 0))
        self.year_label_frame = ttk.Frame(self.year_frame, style='DarkFrame.TFrame')
        self.year_label_frame.pack(side='top', fill='x')
        self.year_label = ttk.Label(self.year_label_frame,
                                    text='Year selection:',
                                    style='ExtraLargeLabel.TLabel')
        self.year_label.pack(side='left', padx=(10, 0), pady=(5, 5))
        self.year_combobox = ttk.Combobox(self.year_frame,
                                          style='Standard.TCombobox',
                                          values=self.E6_years,
                                          state='readonly')
        self.year_combobox.current(0)
        self.year_combobox.pack(side='top', fill='x', padx=(10, 10), pady=(10, 0))

        # Plot options section widgets:
        self.plot_options_label_frame = ttk.Frame(self.plot_options_frame, style='DarkFrame.TFrame')
        self.plot_options_label_frame.pack(side='top', fill='x')
        self.plot_options_label = ttk.Label(self.plot_options_label_frame,
                                            style='ExtraLargeLabel.TLabel',
                                            text='Plot options:')
        self.plot_options_label.pack(side='left', padx=(10, 0), pady=(5, 5))

        # Plot control subframes:
        self.master_controller_frame = ttk.Frame(self.plot_control_frame, style='Standard.TFrame')
        self.master_controller_frame.pack(side='top', fill='x', pady=(20, 0))
        self.master_controller_frame.grid_columnconfigure(1, weight=1)
        self.regular_animated_plots_frame = ttk.Frame(self.plot_control_frame, style='Standard.TFrame')
        self.regular_animated_plots_frame.pack(side='top', fill='x', pady=(20, 0))
        self.regular_plots_frame = ttk.Frame(self.regular_animated_plots_frame, style='Standard.TFrame')
        self.regular_plots_frame.pack(side='left', fill='y')
        self.regular_plots_frame.grid_columnconfigure(1, weight=1)
        self.animated_plots_frame = ttk.Frame(self.regular_animated_plots_frame, style='Standard.TFrame')
        self.animated_plots_frame.pack(side='left', fill='both', expand=True, padx=(10, 0))
        self.animated_plots_frame.grid_columnconfigure(1, weight=1)

        # Master control section widgets:
        self.master_controller_label_frame = ttk.Frame(self.master_controller_frame, style='DarkFrame.TFrame')
        self.master_controller_label_frame.grid(row=0, column=0, columnspan=2, sticky='nsew')
        self.master_control_label = ttk.Label(self.master_controller_label_frame,
                                              text='Master control:',
                                              style='ExtraLargeLabel.TLabel')
        self.master_control_label.pack(side='left', padx=(10, 0), pady=(5, 5))

        self.plot_active_year_label = ttk.Label(self.master_controller_frame,
                                                style='LeftAligned.TLabel',
                                                text='plot active year:')
        self.plot_active_year_label.grid(row=1, column=0, sticky='w', padx=(20, 0), pady=(10, 0))
        self.plot_active_year_button = ttk.Button(self.master_controller_frame,
                                                  style='Standard.TButton',
                                                  text='plot',
                                                  width=6,
                                                  takefocus=False,
                                                  command=self.plot_active_year)
        self.plot_active_year_button.grid(row=1, column=1, sticky='w', padx=(20, 0), pady=(10, 0))

        self.plot_active_testsite_label = ttk.Label(self.master_controller_frame,
                                                    style='LeftAligned.TLabel',
                                                    text='plot active testsite:')
        self.plot_active_testsite_label.grid(row=2, column=0, sticky='w', padx=(20, 0), pady=(10, 0))
        self.plot_active_testsite_button = ttk.Button(self.master_controller_frame,
                                                      style='Standard.TButton',
                                                      text='plot',
                                                      width=6,
                                                      takefocus=False,
                                                      command=self.plot_active_testssite)
        self.plot_active_testsite_button.grid(row=2, column=1, sticky='w', padx=(20, 0), pady=(10, 0))

        self.plot_active_testsites_label = ttk.Label(self.master_controller_frame,
                                                     style='LeftAligned.TLabel',
                                                     text='plot all testsites:')
        self.plot_active_testsites_label.grid(row=3, column=0, sticky='w', padx=(20, 0), pady=(10, 0))
        self.plot_active_testsites_button = ttk.Button(self.master_controller_frame,
                                                       style='Standard.TButton',
                                                       text='plot',
                                                       width=6,
                                                       takefocus=False,
                                                       command=self.plot_all_testsites)
        self.plot_active_testsites_button.grid(row=3, column=1, sticky='w', padx=(20, 0), pady=(10, 0))

        # Regular plot control section widgets:
        self.regular_plots_label_frame = ttk.Frame(self.regular_plots_frame,
                                                   style='DarkFrame.TFrame')
        self.regular_plots_label_frame.grid(row=0, column=0, columnspan=2, sticky='nsew')
        self.regular_plots_label = ttk.Label(self.regular_plots_label_frame,
                                             text='Combined plots:',
                                             style='ExtraLargeLabel.TLabel')
        self.regular_plots_label.pack(side='left', padx=(10, 0), pady=(5, 5))

        self.plot_all_regular_label = ttk.Label(self.regular_plots_frame,
                                                style='LeftAligned.TLabel',
                                                text='plot all:')
        self.plot_all_regular_label.grid(row=1, column=0, sticky='w', padx=(20, 0), pady=(10, 0))
        self.plot_all_regular_button = ttk.Button(self.regular_plots_frame,
                                                  style='Standard.TButton',
                                                  text='plot',
                                                  width=6,
                                                  takefocus=False,
                                                  command=self.plot_all_regular)
        self.plot_all_regular_button.grid(row=1, column=1, sticky='w', padx=(20, 5), pady=(10, 0))

        self.plot_frost_penetration_label = ttk.Label(self.regular_plots_frame,
                                                      style='LeftAligned.TLabel',
                                                      text='frost penetration:')
        self.plot_frost_penetration_label.grid(row=2, column=0, sticky='w', padx=(20, 0), pady=(10, 0))
        self.plot_frost_penetration_button = ttk.Button(self.regular_plots_frame,
                                                        style='Standard.TButton',
                                                        text='plot',
                                                        width=6,
                                                        takefocus=False,
                                                        command=self.plot_frost_penetration)
        self.plot_frost_penetration_button.grid(row=2, column=1, sticky='w', padx=(20, 5), pady=(10, 0))

        self.plot_air_temperature_label = ttk.Label(self.regular_plots_frame,
                                                    style='LeftAligned.TLabel',
                                                    text='air temperature:')
        self.plot_air_temperature_label.grid(row=3, column=0, sticky='w', padx=(20, 0), pady=(10, 0))
        self.plot_air_temperature_button = ttk.Button(self.regular_plots_frame,
                                                      style='Standard.TButton',
                                                      text='plot',
                                                      width=6,
                                                      takefocus=False,
                                                      command=self.plot_air_temperature)
        self.plot_air_temperature_button.grid(row=3, column=1, sticky='w', padx=(20, 5), pady=(10, 0))

        self.plot_freezing_index_label = ttk.Label(self.regular_plots_frame,
                                                   style='LeftAligned.TLabel',
                                                   text='freezing index:')
        self.plot_freezing_index_label.grid(row=4, column=0, sticky='w', padx=(20, 0), pady=(10, 0))
        self.plot_freezing_index_button = ttk.Button(self.regular_plots_frame,
                                                     style='Standard.TButton',
                                                     text='plot',
                                                     width=6,
                                                     takefocus=False,
                                                     command=self.plot_freezing_index)
        self.plot_freezing_index_button.grid(row=4, column=1, sticky='w', padx=(20, 5), pady=(10, 0))

        self.plot_selected_gradients_label = ttk.Label(self.regular_plots_frame,
                                                       style='LeftAligned.TLabel',
                                                       text='selected gradients:')
        self.plot_selected_gradients_label.grid(row=5, column=0, sticky='w', padx=(20, 0), pady=(10, 0))
        self.plot_selected_gradients_button = ttk.Button(self.regular_plots_frame,
                                                         style='Standard.TButton',
                                                         text='plot',
                                                         width=6,
                                                         takefocus=False,
                                                         command=self.plot_selected_gradients)
        self.plot_selected_gradients_button.grid(row=5, column=1, sticky='w', padx=(20, 5), pady=(10, 0))

        # Animated plot control section widgets:
        self.animated_plots_label_frame = ttk.Frame(self.animated_plots_frame,
                                                    style='DarkFrame.TFrame')
        self.animated_plots_label_frame.grid(row=0, column=0, columnspan=2, sticky='nsew')
        self.animated_plots_label = ttk.Label(self.animated_plots_label_frame,
                                              text='Animated plots:',
                                              style='ExtraLargeLabel.TLabel')
        self.animated_plots_label.pack(side='left', padx=(10, 0), pady=(5, 5))

        self.animated_temperature_gradient_label = ttk.Label(self.animated_plots_frame,
                                                             style='LeftAligned.TLabel',
                                                             text='temperature series:')
        self.animated_temperature_gradient_label.grid(row=1, column=0, sticky='w', padx=(20, 0), pady=(10, 0))
        self.animated_temperature_gradient_button = ttk.Button(self.animated_plots_frame,
                                                               style='Standard.TButton',
                                                               text='plot',
                                                               width=6,
                                                               takefocus=False,
                                                               command=self.animated_temperature_gradient)
        self.animated_temperature_gradient_button.grid(row=1, column=1, sticky='w', padx=(20, 5), pady=(10, 0))

        self.animated_frost_progression_label = ttk.Label(self.animated_plots_frame,
                                                          style='LeftAligned.TLabel',
                                                          text='temperature gradient:')
        self.animated_frost_progression_label.grid(row=2, column=0, sticky='w', padx=(20, 0), pady=(10, 0))
        self.animated_frost_progression_button = ttk.Button(self.animated_plots_frame,
                                                            style='Standard.TButton',
                                                            text='plot',
                                                            width=6,
                                                            takefocus=False,
                                                            command=self.animated_frost_progression)
        self.animated_frost_progression_button.grid(row=2, column=1, sticky='w', padx=(20, 5), pady=(10, 0))

    def update_combobox(self):
        if self.testsite_var.get() == self.E6_data.testsite_dir['name']:
            self.year_combobox['values'] = self.E6_years
            self.year_combobox.current(0)
            self.active_testsite = self.E6_data
        elif self.testsite_var.get() == self.Roros_data.testsite_dir['name']:
            self.year_combobox['values'] = self.Roros_years
            self.year_combobox.current(0)
            self.active_testsite = self.Roros_data
        elif self.testsite_var.get() == self.Finland_data.testsite_dir['name']:
            self.year_combobox['values'] = self.Finland_years
            self.year_combobox.current(0)
            self.active_testsite = self.Finland_data
        elif self.testsite_var.get() == self.Sweden_data.testsite_dir['name']:
            self.year_combobox['values'] = self.Sweden_years
            self.year_combobox.current(0)
            self.active_testsite = self.Sweden_data

    def plot_active_year(self):
        selected_year = self.year_combobox.get()

        def retrieve_data(selected_year):
            for year in self.active_testsite.year_list:
                if selected_year == year['year_name']:
                    return year

        data = retrieve_data(selected_year)



    def plot_active_testssite(self):
        print('2')

    def plot_all_testsites(self):
        print('3')

    def plot_all_regular(self):
        print('4')

    def plot_frost_penetration(self):
        print('5')

    def plot_air_temperature(self):
        print('6')

    def plot_freezing_index(self):
        print('7')

    def plot_selected_gradients(self):
        print('8')

    def animated_temperature_gradient(self):
        print('9')

    def animated_frost_progression(self):
        print('10')


def main():
    root = MainApp()
    style = ttk.Style()
    StyleConfiguration(style)
    root.mainloop()


main()
