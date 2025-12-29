# ``WKInternalsNotes/WKMouseInteraction/_setupMouseMovedHandlerForMouse(_:)``

GCMouse の移動ハンドラを差し替える。

## Objective-C Declaration
```objective-c
- (void)_setupMouseMovedHandlerForMouse:(GCMouse *)mouse;
```

## Discussion
`mouse` が `nil` の場合は何もしない。元の `mouseMovedHandler` を保存し、新しいハンドラで `handleGameControllerMouseMove` を呼ぶ。

## References
- [`WKMouseInteraction.mm#L539`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.mm#L539)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
