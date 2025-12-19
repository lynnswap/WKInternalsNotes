# ``WKInternalsNotes/WKContentView/_enableInspectorNodeSearch()``

インスペクタのノード検索モードを有効化する。

## Objective-C Declaration
```objective-c
- (void)_enableInspectorNodeSearch;
```

## Discussion
フラグを立てて既存のジェスチャを外し、`WKInspectorNodeSearchGestureRecognizer` を追加する。

## References
- [`WKContentViewInteraction.h#L842`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L842)
- [`WKContentViewInteraction.mm#L1880`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L1880)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
