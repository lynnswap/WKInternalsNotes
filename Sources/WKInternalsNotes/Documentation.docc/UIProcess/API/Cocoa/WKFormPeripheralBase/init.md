# ``WKInternalsNotes/WKFormPeripheralBase/init()``

デフォルト初期化は利用不可。

## Objective-C Declaration
```objective-c
- (instancetype)init NS_UNAVAILABLE;
```

## Discussion
`NS_UNAVAILABLE` のため使用できない。`initWithView:control:` を使う。

## References
- [`WKFormPeripheralBase.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheralBase.h#L36)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
