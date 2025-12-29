# ``WKInternalsNotes/WKFormPeripheralBase/view``

関連付けられた `WKContentView` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKContentView *view;
```

## Default Value
`initWithView:control:` で指定した `view`。

## Discussion
初期化時に受け取った `view` を保持して返す。

## References
- [`WKFormPeripheralBase.mm#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheralBase.mm#L39)
- [`WKFormPeripheralBase.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheralBase.h#L37)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
