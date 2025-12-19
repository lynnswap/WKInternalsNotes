# ``WKInternalsNotes/WKContentView/_formControlRefreshEnabled()``

フォームコントロールのリフレッシュ可否を返す。

## Objective-C Declaration
```objective-c
- (BOOL)_formControlRefreshEnabled;
```

## Discussion
`_page` が存在する場合のみ `YES` を返す単純なチェック。

## References
- [`WKContentViewInteraction.h#L975`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L975)
- [`WKContentViewInteraction.mm#L8202`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L8202)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
