# ``WKInternalsNotes/WKActionSheetAssistant/showMediaControlsContextMenu(_:items:completionHandler:)``

メディアコントロール用のコンテキストメニューを表示する。

## Objective-C Declaration
```objective-c
- (void)showMediaControlsContextMenu:(WebCore::FloatRect&&)targetFrame items:(Vector<WebCore::MediaControlsContextMenuItem>&&)items completionHandler:(CompletionHandler<void(WebCore::MediaControlsContextMenuItem::ID)>&&)completionHandler;
```

## Discussion
項目リストから `UIMenu` を構築し、必要に応じてデリゲートの追加項目を合成する。表示条件を満たさない場合は `completionHandler` に `invalidID` を返し、それ以外はコールバックと対象矩形を保持してプレゼンターで表示する。

## References
- [`WKActionSheetAssistant.h#L117`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L117)
- [`WKActionSheetAssistant.mm#L857`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.mm#L857)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
