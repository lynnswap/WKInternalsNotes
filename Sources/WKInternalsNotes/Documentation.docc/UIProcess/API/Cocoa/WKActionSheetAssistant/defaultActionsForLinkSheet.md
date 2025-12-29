# ``WKInternalsNotes/WKActionSheetAssistant/defaultActionsForLinkSheet(_:)``

リンク向けの既定アクション一覧を生成する。

## Objective-C Declaration
```objective-c
- (RetainPtr<NSArray<_WKElementAction *>>)defaultActionsForLinkSheet:(_WKActivatedElementInfo *)elementInfo;
```

## Discussion
URLを取得できない場合は `nil` を返す。取得できた場合は「開く」などを追加し、Reading List対応や画像/写真アクセス、画像解析の可用性に応じてアクションを追加し、アニメーション操作も付与して返す。

## References
- [`WKActionSheetAssistant.h#L121`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L121)
- [`WKActionSheetAssistant.mm#L553`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.mm#L553)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
