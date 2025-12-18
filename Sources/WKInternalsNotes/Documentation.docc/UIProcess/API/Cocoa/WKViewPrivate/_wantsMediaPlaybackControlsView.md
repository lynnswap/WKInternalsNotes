# ``WKInternalsNotes/WKView/_wantsMediaPlaybackControlsView``

メディア再生コントロールを要求するか返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readwrite, setter=_setWantsMediaPlaybackControlsView:) BOOL _wantsMediaPlaybackControlsView;
```

## Default Value
`NO`。

## Discussion
getter は `NO` を返し、setter は空実装。

## References
- [`WKViewPrivate.h#L137`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L137)
- [`WKView.mm#L1354`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1354)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
