# ``WKInternalsNotes/WKContentView/preventsPanningInXAxis``

水平方向のパン操作を抑制しているかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL preventsPanningInXAxis;
```

## Default Value
`_preventsPanningInXAxis` を返す。

## Discussion
内部フラグ `_preventsPanningInXAxis` の値を返す。

## References
- [`WKContentViewInteraction.h#L350`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L350)
- [`WKContentViewInteraction.mm#L1159`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L1159)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
