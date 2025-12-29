# ``WKInternalsNotes/WKARPresentationSession/sessionEndRequested``

セッション終了要求が出ているかを示す。

## Objective-C Declaration
```objective-c
@property (atomic, readonly, getter=isSessionEndRequested) BOOL sessionEndRequested;
```

## Default Value
`NO`。

## Discussion
初期化時に `NO` を設定し、キャンセル操作で `YES` に更新される。

## References
- [`WKARPresentationSession.mm#L143`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.mm#L143)
- [`WKARPresentationSession.mm#L146`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.mm#L146)
- [`WKARPresentationSession.mm#L321`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.mm#L321)
- [`WKARPresentationSession.h#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.h#L53)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
