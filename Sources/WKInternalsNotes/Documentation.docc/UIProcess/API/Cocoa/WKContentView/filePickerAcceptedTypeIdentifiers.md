# ``WKInternalsNotes/WKContentView/filePickerAcceptedTypeIdentifiers()``

ファイルピッカーが受け付ける UTI/UTType 識別子配列を返す。

## Objective-C Declaration
```objective-c
- (NSArray<NSString *> *)filePickerAcceptedTypeIdentifiers;
```

## Discussion
`_fileUploadPanel` が無い場合は空配列を返し、存在する場合は `acceptedTypeIdentifiers` を返す。

## References
- [`WKContentViewInteraction.h#L838`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L838)
- [`WKContentViewInteraction.mm#L7822`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L7822)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
