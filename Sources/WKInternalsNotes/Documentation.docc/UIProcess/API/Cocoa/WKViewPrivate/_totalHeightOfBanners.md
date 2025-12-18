# ``WKInternalsNotes/WKView/_totalHeightOfBanners``

バナー領域の合計高さを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setTotalHeightOfBanners:) CGFloat _totalHeightOfBanners;
```

## Default Value
`0`。

## Discussion
getter は `0` を返し、setter は空実装。

## References
- [`WKViewPrivate.h#L71`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L71)
- [`WKView.mm#L1232`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1232)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
