# ``WKInternalsNotes/_WKModalContainerInfo/initWithTypes(_:)``

`WebCore` の型集合を `_WKModalContainerControlTypes` に変換する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithTypes:(OptionSet<WebCore::ModalContainerControlType>)types;
```

## Discussion
`types` の `Positive`/`Negative`/`Neutral` をそれぞれ `_availableTypes` に OR して保持する。

## References
- [`_WKModalContainerInfoInternal.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKModalContainerInfoInternal.h#L37)
- [`_WKModalContainerInfo.mm#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKModalContainerInfo.mm#L33)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
