# ``WKInternalsNotes/WKContentView/_showMediaControlsContextMenu(_:items:completionHandler:)``

メディアコントロールのコンテキストメニューを表示する。

## Objective-C Declaration
```objective-c
- (void)_showMediaControlsContextMenu:(WebCore::FloatRect&&)targetFrame items:(Vector<WebCore::MediaControlsContextMenuItem>&&)items completionHandler:(CompletionHandler<void(WebCore::MediaControlsContextMenuItem::ID)>&&)completionHandler;
```

## Discussion
`WKActionSheetAssistant` にメニュー表示を委譲し、選択結果を `completionHandler` に返す。

## References
- [`WKContentViewInteraction.h#L972`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L972)
- [`WKContentViewInteraction.mm#L12258`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L12258)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
