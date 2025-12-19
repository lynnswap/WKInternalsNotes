# ``WKInternalsNotes/WKContentView/preventsPanningInYAxis``

垂直方向のパン操作を抑制しているかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL preventsPanningInYAxis;
```

## Default Value
`_preventsPanningInYAxis` を返す。

## Discussion
内部フラグ `_preventsPanningInYAxis` の値を返す。

## References
- [`WKContentViewInteraction.h#L351`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L351)
- [`WKContentViewInteraction.mm#L1164`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L1164)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
