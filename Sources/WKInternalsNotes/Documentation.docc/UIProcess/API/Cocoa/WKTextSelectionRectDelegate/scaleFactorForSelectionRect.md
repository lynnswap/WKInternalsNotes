# ``WKInternalsNotes/WKTextSelectionRectDelegate/scaleFactorForSelectionRect(_:)``

選択矩形のスケール係数を返す。

## Objective-C Declaration
```objective-c
- (CGFloat)scaleFactorForSelectionRect:(WKTextSelectionRect *)rect;
```

## Discussion
`WKContentViewInteraction` は `self._contentZoomScale` を返す。

## References
- [`WKTextSelectionRect.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKTextSelectionRect.h#L42)
- [`WKContentViewInteraction.mm#L6501`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L6501)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
