# ``WKInternalsNotes/WKFormPeripheralBase/control``

フォーム制御用の `WKFormControl` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSObject <WKFormControl> *control;
```

## Default Value
初期化時に渡された `control`。

## Discussion
`initWithView:control:` で保持した `_control` を返す。

## References
- [`WKFormPeripheralBase.mm#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheralBase.mm#L39)
- [`WKFormPeripheralBase.mm#L80`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheralBase.mm#L80)
- [`WKFormPeripheralBase.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheralBase.h#L37)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
