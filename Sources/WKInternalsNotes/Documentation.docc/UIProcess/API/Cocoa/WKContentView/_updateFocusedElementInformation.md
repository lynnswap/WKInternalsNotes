# ``WKInternalsNotes/WKContentView/_updateFocusedElementInformation(_:)``

フォーカス要素の情報を更新する。

## Objective-C Declaration
```objective-c
- (void)_updateFocusedElementInformation:(const WebKit::FocusedElementInformation&)information;
```

## Discussion
現在のフォーカス要素と同一の `elementContext` であれば情報を更新し、入力周辺 UI を再同期する。

## References
- [`WKContentViewInteraction.h#L811`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L811)
- [`WKContentViewInteraction.mm#L8718`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L8718)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
