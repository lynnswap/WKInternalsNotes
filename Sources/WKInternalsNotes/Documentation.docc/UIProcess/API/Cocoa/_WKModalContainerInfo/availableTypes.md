# ``WKInternalsNotes/_WKModalContainerInfo/availableTypes``

利用可能なボタン種別のビットマスク。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) _WKModalContainerControlTypes availableTypes;
```

## Default Value
`initWithTypes:` で設定される。

## Discussion
`WebCore::ModalContainerControlType` の `OptionSet` を `_WKModalContainerControlTypes` に変換した結果を保持する。

## References
- [`_WKModalContainerInfo.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKModalContainerInfo.h#L38)
- [`_WKModalContainerInfo.mm#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKModalContainerInfo.mm#L33)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
