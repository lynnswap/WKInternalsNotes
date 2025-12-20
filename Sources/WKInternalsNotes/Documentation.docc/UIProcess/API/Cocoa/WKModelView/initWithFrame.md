# ``WKInternalsNotes/WKModelView/initWithFrame(_:)``

この初期化子は使用不可。

## Objective-C Declaration
```objective-c
- (instancetype)initWithFrame:(CGRect)frame NS_UNAVAILABLE;
```

## Discussion
`NS_UNAVAILABLE` のため使用できない。実装でも `nil` を返す。

## References
- [`WKModelView.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKModelView.h#L45)
- [`WKModelView.mm#L65`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKModelView.mm#L65)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
