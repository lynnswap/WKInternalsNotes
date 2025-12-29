# ``WKInternalsNotes/_WKFormInputSession/focusedElementInfo``

フォーカス中の要素情報を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) id <_WKFocusedElementInfo> focusedElementInfo WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
初期化時に渡された `WKFocusedElementInfo`。

## Discussion
`WKFormInputSession` の初期化で保持した `WKFocusedElementInfo` を返す。

## References
- [`WKContentViewInteraction.mm#L775`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L775)
- [`WKContentViewInteraction.mm#L787`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L787)
- [`_WKFormInputSession.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFormInputSession.h#L37)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
