# ``WKInternalsNotes/WKContentView/_elementDidFocus(_:userIsInteracting:blurPreviousNode:activityStateChanges:userObject:)``

フォーカスされた要素の情報を反映し、入力セッションを開始する。

## Objective-C Declaration
```objective-c
- (void)_elementDidFocus:(const WebKit::FocusedElementInformation&)information userIsInteracting:(BOOL)userIsInteracting blurPreviousNode:(BOOL)blurPreviousNode activityStateChanges:(OptionSet<WebCore::ActivityState>)activityStateChanges userObject:(NSObject <NSSecureCoding> *)userObject;
```

## Discussion
フォーカス状態フラグを更新し、`WKFocusedElementInfo` を生成して input delegate に入力セッション開始可否を問い合わせる。結果に応じてキーボード/入力ビューの表示やアクセサリ更新を行い、必要なら前の要素の blur を伴うフォーカス切り替えを処理する。

## References
- [`WKContentViewInteraction.h#L808`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L808)
- [`WKContentViewInteraction.mm#L8335`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L8335)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
