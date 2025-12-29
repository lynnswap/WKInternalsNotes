# ``WKInternalsNotes/WKTextFinderClient/didGetImageForMatchResult(_:)``

検索結果の画像取得完了を通知する。

## Objective-C Declaration
```objective-c
- (void)didGetImageForMatchResult:(WebKit::WebImage *)string;
```

## Discussion
コールバック待ちがなければ何もしない。`WebImage` を `NSImage` に変換して先頭の画像コールバックに渡す。

## References
- [`WKTextFinderClient.mm#L57`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKTextFinderClient.mm#L57)
- [`WKTextFinderClient.mm#L309`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKTextFinderClient.mm#L309)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
