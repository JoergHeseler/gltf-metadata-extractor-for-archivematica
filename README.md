# glTF Metadata Extractor for Archivematica

This repository provides a script to extract metadata from Graphics Language Transmission Format (glTF) files in [Archivematica](https://www.archivematica.org/) using the official [glTF-Validator](https://github.com/KhronosGroup/glTF-Validator/releases) tool.

## Installation

To install this script, follow these steps:

### 1. Download the official glTF-Validator tool

- Download the latest release of the [glTF-Validator](https://github.com/KhronosGroup/glTF-Validator/releases) and install it in the `/usr/share/` folder.

### 2. Create a new format policy tool

- In the Archivematica frontend, navigate to **Preservation planning** > **Format policy registry** > **Tools** > **Create new tool** or go directly to [this link](http://10.10.10.20/fpr/fptool/create/).
- Enter the following parameters:
  - **Description**: Enter `gltf_validator`.
  - **Version**: Enter the version you downloaded, e. g. `2.0.0-dev.3.8`.
- Click **Save**.

### 3. Create a new characterization command

- In the Archivematica frontend, navigate to **Preservation planning** > **Characterization** > **Commands** > **Create new command** or go directly to [this link](http://10.10.10.20/fpr/fpcommand/create/).
- Fill in the following fields:
  - **The related tool**: Select **gltf_validator**.
  - **Description**: Enter `Characterize using gltf_validator`.
  - **Command**: Paste the entire content of the [**gltf-metadata-extractor.py**](./src/gltf-metadata-extractor.py) file.
  - **Script type**: Select **Python script**.
  - **The related output format**: Select **Text (Markup): XML: XML (fmt/101)**.
  - **Command usage**: Select **Characterization**.
  - Leave all other input fields and combo boxes untouched.
- Click **Save**.

### 4. Create a new characterization rule for ASCII based glTF 1.0

- In the Archivematica frontend, navigate to **Preservation planning** > **Characterization** > **Rules** > **Create new rule** or go directly to [this link](http://10.10.10.20/fpr/fprule/create/).
- Fill in the following fields:
  - **Purpose**: Select **Characterization**.
  - **The related format**: Select **Model: GL Transmission Format (Text): GLTF 1.0 (fmt/1314)**.
  - **Command**: Select **Characterize using gltf_validator**.
- Click **Save**.

### 5. Create a new characterization rule for ASCII based glTF 2.0

- In the Archivematica frontend, navigate to **Preservation planning** > **Characterization** > **Rules** > **Create new rule** or go directly to [this link](http://10.10.10.20/fpr/fprule/create/).
- Fill in the following fields:
  - **Purpose**: Select **Characterization**.
  - **The related format**: Select **Model: GL Transmission Format (Text): GLTF 2.0 (fmt/1315)**.
  - **Command**: Select **Characterize using gltf_validator**.
- Click **Save**.

### 6. Create a new characterization rule for binary glTF files

- In the Archivematica frontend, navigate to **Preservation planning** > **Characterization** > **Rules** > **Create new rule** or go directly to [this link](http://10.10.10.20/fpr/fprule/create/).
- Fill in the following fields:
  - **Purpose**: Select **Characterization**.
  - **The related format**: Select **Model: GL Transmission Format (Binary): GLTF (Binary) (fmt/1316)**.
  - **Command**: Select **Characterize using gltf_validator**.
- Click **Save**.

## Test

To test this metadata exctractor, you can use the sample glTF files located [here](https://github.com/JoergHeseler/mesh-samples-for-preservation-testing/tree/main/gltf).

### In Archivematica:

You can view the error codes and detailed characterization results in the Archivmatica frontend after starting a transfer by expanding the `▸ Microservice: Characterize and extract metadata` section and clicking on the gear icon of `Microservice: Characterize and extract metadata`.

Valid files should pass characterization with this script and return error code **0**. However, files containing errors should fail characterization and either return error code **1** or **255**.

### In the command line:

You can use the validator at the command line prompt by typing `python gltf-metadata-extractor.py --file-full-name=<GLTF file to characterize>`. You may also want to add `--validator-path=<path to the official gltf_validator>`.

### Example

If you use this script to characterize the ASCII embedded glTF 2.0 model [`cockatoo-gltf-2.0_separated-valid.gltf`](https://github.com/JoergHeseler/3d-sample-files-for-digital-preservation-testing/blob/main/gltf/cockatoo-gltf-2.0_separated-valid/cockatoo-gltf-2.0_separated-valid.gltf), the error code **0** should be returned and the following XML content will be included in the AIP's METS document in the <objectCharacteristicsExtension> element of the file:

```xml
<?xml version="1.0" ?>
<GLTFMetadataExtractor xmlns="http://nfdi4culture.de/gltf-metadata-extractor1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://nfdi4culture.de/gltf-metadata-extractor1 https://raw.githubusercontent.com/JoergHeseler/gltf-metadata-extractor-for-archivematica/refs/heads/main/src/gltf-metadata-extractor.xsd">
    <formatName>glTF (Graphics Library Transmission Format)</formatName>
    <formatVersion>2.0</formatVersion>
    <size>11090</size>
    <SHA256Checksum>a687aa792ee2fa6fd4c8a4c4ce116edc0d09a79e520de8caae662d44140ae5f8</SHA256Checksum>
    <creationDate>2024-12-13T10:03:42.166498</creationDate>
    <modificationDate>2024-12-13T13:28:35.842678</modificationDate>
    <generator>Khronos glTF Blender I/O v4.3.47</generator>
    <hasDefaultScene>true</hasDefaultScene>
    <totalVertexCount>519913</totalVertexCount>
    <totalTriangleCount>776822</totalTriangleCount>
    <materialCount>1</materialCount>
    <hasTextures>true</hasTextures>
    <animationCount>0</animationCount>
    <hasSkins>false</hasSkins>
    <rawGLTFValidatorOutput><![CDATA[{
    "uri": "var/archivematica/sharedDirectory/watchedDirectories/workFlowDecisions/extractPackagesChoice/g16_test-dd341170-fea6-4371-9198-5a5dc79b2fe7/objects/cockatoo-gltf-2.0_separated-valid.gltf",
    "mimeType": "model/gltf+json",
    "validatorVersion": "2.0.0-dev.3.8",
    "issues": {
        "numErrors": 0,
        "numWarnings": 0,
        "numInfos": 0,
        "numHints": 0,
        "messages": [],
        "truncated": false
    },
    "info": {
        "version": "2.0",
        "generator": "Khronos glTF Blender I/O v4.3.47",
        "extensionsUsed": [
            "KHR_materials_specular"
        ],
        "resources": [
            {
                "pointer": "/buffers/0",
                "mimeType": "application/gltf-buffer",
                "storage": "external",
                "uri": "cockatoo-gltf-2.0_separated-valid.bin",
                "byteLength": 25589552
            },
            {
                "pointer": "/images/0",
                "mimeType": "image/png",
                "storage": "external",
                "uri": "Image_2.png",
                "image": {
                    "width": 1024,
                    "height": 1024,
                    "format": "rgb",
                    "primaries": "srgb",
                    "transfer": "srgb",
                    "bits": 8
                }
            },
            {
                "pointer": "/images/1",
                "mimeType": "image/jpeg",
                "storage": "external",
                "uri": "Image_0.jpg",
                "image": {
                    "width": 1024,
                    "height": 1024,
                    "format": "rgb",
                    "bits": 8
                }
            },
            {
                "pointer": "/images/2",
                "mimeType": "image/png",
                "storage": "external",
                "uri": "Image_1.png",
                "image": {
                    "width": 1024,
                    "height": 1024,
                    "format": "rgb",
                    "primaries": "srgb",
                    "transfer": "srgb",
                    "bits": 8
                }
            }
        ],
        "animationCount": 0,
        "materialCount": 1,
        "hasMorphTargets": false,
        "hasSkins": false,
        "hasTextures": true,
        "hasDefaultScene": true,
        "drawCallCount": 8,
        "totalVertexCount": 519913,
        "totalTriangleCount": 776822,
        "maxUVs": 1,
        "maxInfluences": 0,
        "maxAttributes": 3
    }
}]]></rawGLTFValidatorOutput>
</GLTFMetadataExtractor>
```

## Dependencies

[Archivematica 1.13.2](https://github.com/artefactual/archivematica/releases/tag/v1.13.2) and [glTF-Validator 2.0.0-dev.3.8](https://github.com/KhronosGroup/glTF-Validator/releases/tag/2.0.0-dev.3.8) were used to analyze, design, develop and test this script.

## Background

As part of the [NFDI4Culture](https://nfdi4culture.de/) initiative, efforts are underway to enhance the capabilities of open-source digital preservation software like Archivematica to identify, validate and characterize 3D file formats. This repository provides a script to improve metadata extraction of Graphics Language Transmission Format (glTF) files in Archivematica, enhancing its 3D content preservation capabilities.

## Related projects

- [DAE Validator for Archivematica](https://github.com/JoergHeseler/dae-validator-for-archivematica)
- [glTF Validator for Archivematica](https://github.com/JoergHeseler/gltf-validator-for-archivematica)
- [Mesh Samples for Preservation Testing](https://github.com/JoergHeseler/mesh-samples-for-preservation-testing)
- [Point Cloud Samples for Digital Preservation Testing](https://github.com/JoergHeseler/point-cloud-samples-for-preservation-testing)
- [Siegfried Falls Back on Fido Identifier for Archivematica](https://github.com/JoergHeseler/siegfried-falls-back-on-fido-identifier-for-archivematica)
- [STL Cleaner](https://github.com/JoergHeseler/stl-cleaner)
- [STL Metadata Extractor for Archivematica](https://github.com/JoergHeseler/stl-metadata-extractor-for-archivematica)
- [STL Validator for Archivematica](https://github.com/JoergHeseler/stl-validator-for-archivematica)
- [X3D Validator for Archivematica](https://github.com/JoergHeseler/x3d-validator-for-archivematica)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Acknowledgments

Special thanks to the colleagues from the SLUB Dresden, specifically from the Infrastructure and Long-Term Availability division, for their support and valuable feedback during the development.

## Imprint

[NFDI4Culture](https://nfdi4culture.de/) – Consortium for Research Data on Material and Immaterial Cultural Heritage.  
Funded by the German Research Foundation (DFG), Project No. [441958017](https://gepris.dfg.de/gepris/projekt/441958017).

**Author**: [Jörg Heseler](https://orcid.org/0000-0002-1497-627X)  
**License**: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
