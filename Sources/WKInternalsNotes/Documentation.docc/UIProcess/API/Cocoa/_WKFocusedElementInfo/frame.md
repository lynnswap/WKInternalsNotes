# ``WKInternalsNotes/_WKFocusedElementInfo/frame``

要素が属するフレーム情報を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) WKFrameInfo *frame WK_API_AVAILABLE(macos(26.0), ios(26.0), visionos(26.0));
```

## Default Value
`FocusedElementInformation::frame` がある場合はその情報から生成された `WKFrameInfo`。無い場合は `nil`。

## Discussion
`information.frame` が存在する場合に `API::FrameInfo` から `WKFrameInfo` を生成して保持し、その値を返す。

## References
- [`_WKFocusedElementInfo.h#L79`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFocusedElementInfo.h#L79)
- [`WKContentViewInteraction.mm#L1024`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L1024)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
