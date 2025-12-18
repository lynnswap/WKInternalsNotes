# ``WKInternalsNotes/WKFrameInfo/_isScrollable``

フレームがスクロール可能かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _isScrollable WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Default Value
`frameMetrics.isScrollable == WebKit::IsScrollable::Yes` の結果。

## Discussion
FrameInfoData の `frameMetrics.isScrollable` を `IsScrollable::Yes` と比較して判定する。

## References
- [`WKFrameInfoPrivate.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKFrameInfoPrivate.h#L42)
- [`WKFrameInfo.mm#L140`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKFrameInfo.mm#L140)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
