from typing import List, Optional, Union, Literal
from pydantic import Field
# Not: SDK yollarını kendi sisteminizdeki gerçek yollara göre güncelleyin
from sdks.novavision.src.base.model import Config, Inputs, Outputs, Request, Response, Package, Configs

# --- ALAN TİPLERİ ---
class TextField(Config):
    name: Literal["MetinAlani"] = "MetinAlani"
    value: str = ""
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

class NumberField(Config):
    name: Literal["SayiAlani"] = "SayiAlani"
    value: float = 0.0
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

# --- DROPDOWN SEÇENEKLERİ ---
class Option1(Config):
    name: Literal["Secenek1"] = "Secenek1"
    field1: TextField  # 1. Tip
    field2: NumberField # 2. Tip
    value: Literal["Secenek1"] = "Secenek1"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

class Option2(Config):
    name: Literal["Secenek2"] = "Secenek2"
    field1: TextField
    field2: NumberField
    value: Literal["Secenek2"] = "Secenek2"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

# --- BAĞIMLI DROPDOWN ---
class MyDependentDropdown(Config):
    name: Literal["dependentDropdown"] = "dependentDropdown"
    value: Union[Option1, Option2]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

class SharedConfigs(Configs):
    dropdown_ayar: MyDependentDropdown

# --- EXECUTOR 1 (1 Giriş, 1 Çıkış) ---
class Ex1Inputs(Inputs):
    in1: TextField

class Ex1Outputs(Outputs):
    out1: TextField

class Ex1Request(Request):
    inputs: Optional[Ex1Inputs]
    configs: SharedConfigs

class Ex1Response(Response):
    outputs: Ex1Outputs

# --- EXECUTOR 2 (2 Giriş, 2 Çıkış) ---
class Ex2Inputs(Inputs):
    in1: TextField
    in2: NumberField

class Ex2Outputs(Outputs):
    out1: TextField
    out2: NumberField

class Ex2Request(Request):
    inputs: Optional[Ex2Inputs]
    configs: SharedConfigs

class Ex2Response(Response):
    outputs: Ex2Outputs

# --- ANA YAPILANDIRMA ---
class FirstExecutor(Config):
    name: Literal["FirstExecutor"] = "FirstExecutor"
    value: Union[Ex1Request, Ex1Response]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"
    class Config:
        schema_extra = {"target": {"value": 0}}

class SecondExecutor(Config):
    name: Literal["SecondExecutor"] = "SecondExecutor"
    value: Union[Ex2Request, Ex2Response]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"
    class Config:
        schema_extra = {"target": {"value": 0}}

class ConfigExecutor(Config):
    name: Literal["ConfigExecutor"] = "ConfigExecutor"
    value: Union[FirstExecutor, SecondExecutor]
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

class PackageConfigs(Configs):
    executor_secimi: ConfigExecutor

class PackageModel(Package):
    configs: PackageConfigs
    type: Literal["capsule"] = "capsule"
    name: Literal["DemoPackage"] = "DemoPackage"